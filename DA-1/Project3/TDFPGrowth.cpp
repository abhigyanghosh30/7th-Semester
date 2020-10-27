#include <bits/stdc++.h>
using namespace std;
map<string, tuple<uint, Node *>> header;
vector<Node *> root;
class Node
{
public:
    string item;
    uint count;
    Node *sidelink;
    Node *parent;
    vector<Node *> children;
    Node()
    {
        this->item = "";
        this->count = 0;
        this->sidelink = NULL;
        this->parent = NULL;
    }
    Node(string item)
    {
        this->item = item;
        this->count = 1;
        this->sidelink = NULL;
        this->parent = NULL;
    }
    Node(string item, uint count)
    {
        this->item = item;
        this->count = count;
        this->sidelink = NULL;
        this->parent = NULL;
    }
    void addChild(string item)
    {
        Node child = Node(item);
        child.parent = this;
        this->children.push_back(&child);
        auto it = header.find(item);
        get<0>(it->second) += 1;
        Node *last = get<1>(it->second);
        while (last != NULL)
        {
            last = last->sidelink;
        }
        last->sidelink = &child;
    }
};

int main()
{
    string sourceFileName = "project3.txt";
    ifstream fin(sourceFileName, ios::in);
    string line, items;
    while (getline(fin, line))
    {
        set<string> values;
        stringstream s(line);
        while (getline(s, items, ' '))
        {
            if (items == "-2")
            {
                break;
            }
            if (items == "-1")
            {
                continue;
            }
            values.insert(items);
            // cout << items << endl;
        }
        }
}