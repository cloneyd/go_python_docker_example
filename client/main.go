package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
)

func main() {
	host := os.Getenv("SERVER_HOST")
	if len(host) == 0 {
		log.Fatalln("server host value is empty")
	}
	port := os.Getenv("SERVER_PORT")
	if len(port) == 0 {
		log.Fatalln("server port value is empty")
	}

	url := fmt.Sprintf("http://%s:%s", host, port)

	resp, err := http.Get(url + "/health")
	if err != nil {
		log.Println(err)

	}
	defer resp.Body.Close()

	if resp.StatusCode == http.StatusOK {
		bodyBytes, err := io.ReadAll(resp.Body)
		if err != nil {
			log.Fatalln(err)
		}
		bodyString := string(bodyBytes)
		log.Println(bodyString)
	}
}
