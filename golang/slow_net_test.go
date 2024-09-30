package golang

import (
	"fmt"
	"io"
	"net"
	"sync"
	"testing"
	"time"
)

func getConnectionSlow() interface{} {
	time.Sleep(1 * time.Second)
	return struct{}{}
}

func webserver() *sync.WaitGroup {
	var wg sync.WaitGroup
	wg.Add(1)

	go func() {
		listen, err := net.Listen("tcp", "0.0.0.0:9002")
		if err != nil {
			fmt.Println("error in listening: slow ", err)
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
			_ = getConnectionSlow()
			fmt.Fprintf(conn, "Hello World")
			conn.Close()
		}
	}()
	return &wg
}

var onceSlow sync.Once

func startupSlow() {
	web := webserver()
	web.Wait()
}

func BenchmarkNetworkReq(b *testing.B) {
	onceSlow.Do(startupSlow)
	fmt.Println("benchmark slow ", b.N)
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
