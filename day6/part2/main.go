// doing this in golang bc multithreading in python sucks ass

package main

import(
    "fmt"
    "strings"
    "strconv"
    "io/ioutil"
)

func getInput() []int {
    content, _ := ioutil.ReadFile("input.txt")
    strlist := strings.Split(string(content), ",")
    ret := []int{}
    for _, i := range strlist {
        x, _ := strconv.Atoi(i)
        ret = append(ret, x)
    }
    return ret
}

func runFishReproduction(fishlist []int) []int {
    l := []int{}
    for _, v := range fishlist {
        if v > 0 {
            l = append(l, v - 1)
        } else {
            l = append(l, []int{6, 8}...)
        }
    }
    return fishlist
}

func main() {
    l := getInput()
    for i := 0; i < 80; i++ {
        l = runFishReproduction(l)
    }
    fmt.Println(len(l))
}