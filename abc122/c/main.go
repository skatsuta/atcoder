package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func atoi(s string) int {
	i, _ := strconv.Atoi(s)
	return i
}

var print = fmt.Println

func main() {
	sc := bufio.NewScanner(os.Stdin)

	sc.Scan()
	sc.Scan()
	S := sc.Text()

	for sc.Scan() {
		ln := strings.Split(sc.Text(), " ")
		l, r := atoi(ln[0]), atoi(ln[1])

		cnt := 0
		s := S[l-1 : r]
		for i := 0; i < len(s)-1; i++ {
			if s[i] == 'A' && s[i+1] == 'C' {
				cnt++
			}
		}

		print(cnt)
	}
}
