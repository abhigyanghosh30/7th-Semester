#include <bits/stdc++.h>
#include "pugixml.hpp"
int main(int argc, char const *argv[])
{
    pugi::xml_document doc;
    pugi::xml_parse_result result = doc.load_file("enwiki-20200801-pages-articles-multistream1.xml");
    std::cout << result.description() << std::endl;
    return 0;
}
