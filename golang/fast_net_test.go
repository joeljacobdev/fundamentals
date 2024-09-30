package golang

import (
	"fmt"
	"io"
	"net"
	"sync"
	"testing"
	"time"
)

func getConnection() interface{} {
	time.Sleep(1 * time.Second)
	return struct{}{}
}

func webserverFast() *sync.WaitGroup {
	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		listen, err := net.Listen("tcp", "0.0.0.0:9002")
		if err != nil {
			fmt.Println("error in listening: fast ", err)
			return
		}
		connPool := getConnectionPool()
		if err != nil {
			return
		}
		defer func(listen net.Listener) {
			err := listen.Close()
			if err != nil {
				fmt.Println("error in closing listener ", err)
				return
			}
		}(listen)
		wg.Done()
		for {
			conn, err := listen.Accept()
			if err != nil {
				fmt.Println("error in connection ", err)
				continue
			}
			c := connPool.Get()
			fmt.Fprintf(conn, "Hello World")
			connPool.Put(c)
			conn.Close()
		}
	}()
	return &wg
}

func getConnectionPool() *sync.Pool {
	pool := sync.Pool{
		New: getConnection,
	}
	for i := 0; i < 10; i++ {
		pool.Put(pool.New())
	}
	return &pool
}

var once sync.Once

func startup() {
	web := webserverFast()
	web.Wait()
}

func BenchmarkNetworkFastReq(b *testing.B) {
	once.Do(startup)
	fmt.Println("benchmark fast ", b.N)
	for i := 0; i < b.N; i++ {
		conn, err := net.Dial("tcp", "0.0.0.0:9002")
		if err != nil {
			b.Fatal("failed to connect ", err)
		}
		if _, err := io.ReadAll(conn); err != nil {
			b.Fatal("cannot read ", err)
		}
		conn.Close()
	}
}
