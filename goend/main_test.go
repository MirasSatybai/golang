package main

import "testing"

func BenchmarkAitbek(b *testing.B) {
	for i := 0; i < b.N; i++ {
		solution1()
	}
}



func BenchmarkModdedSecond(b *testing.B) {
	for i := 0; i < b.N; i++ {
		mysolution()
	}
}


//go test -bench . -benchmem -memprofile=mem.out -memprofilerate=1 -cpuprofile=cpu.out
//go tool pprof mem.out
//go tool pprof cpu.out
