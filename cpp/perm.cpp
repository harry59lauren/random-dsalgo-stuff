#include <iostream>
#include <vector>


std::vector<std::string> perm (std::string s);
//void generate_perms(std::string prefix, std::string rem, int index, std::vector<std::string> &permutations);
void generate_perms(std::string prefix,int index, std::vector<std::string> &permutations);

int main(){

    std::string str = "abcdefh";

    std::vector<std::string> v = perm(str);

    for(std::string s : v)
    std::cout << s << " ";

    std::cout << v.size() << std::endl;

    return 0;
}


std::vector<std::string> perm (std::string s) {
    std::vector<std::string> p;
    generate_perms(s, 0, p);
    return p;
}

void generate_perms(std::string prefix,int index, std::vector<std::string> &permutations){

    if(index == prefix.length())
        permutations.push_back(prefix);
    
    for(int i = index; i < prefix.length(); i++){
        std::swap(prefix[index], prefix[i]);
        generate_perms(prefix, index + 1, permutations);
        std::swap(prefix[index], prefix[i]);
    }
}



