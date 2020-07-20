#include <iostream>


int hammingDistance(int x, int y){
    unsigned int v = x ^ y;
    return ((v & 0xfff) * 0x1001001001001ULL & 0x84210842108421ULL) % 0x1f + (((v & 0xfff000) >> 12) * 0x1001001001001ULL & 0x84210842108421ULL) % 0x1f + ((v >> 24) * 0x1001001001001ULL & 0x84210842108421ULL) % 0x1f;
}

int main(){

    int hd = hammingDistance(1,4);
    std::cout << hd << std::endl;
    return 0;
}