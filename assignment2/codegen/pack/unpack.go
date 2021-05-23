// go build gen/* && ./codegen.exe pack/packer.go  pack/marshaller.go
package main

import "fmt"

type User struct {
	ID       int
	RealName string `cgen:"-"`
	Login    string
	Flags    int
}

type Avatar struct {
	ID  int
	Url string
}

var test = 42

func main() {

	data := []byte{
		128, 36, 17, 0,

		9, 0, 0, 0,
		118, 46, 114, 111, 109, 97, 110, 111, 118,

		16, 0, 0, 0,
	}

	u := User{}
	u.Unpack(data)
	fmt.Printf("Unpacked user %#v", u)
}
