

- [链表中倒数第 k 个节点](#a1)

- [反转链表](#a2)

- [C++ 容器](#a3)

<h2 id='a1'>链表中倒数第 k 个节点</h2>


```cpp
struct ListNode{
	int 		value;
	ListNode*  	next;
};

ListNode* FindKthToTail(ListNode* head, unsigned int k){
    if (!head||k==0) return NULL;
    ListNode* ahead = head;
    for (int i = 0; i < k; ++i) {
        if (ahead->next){
            ahead = ahead->next;
        } else{
            return NULL;
        }
    }
    while(ahead->next){
        ahead = ahead->next;
        head = head->next;
    }
    return head;
}
```


反转链表

```
ListNode* ReverseList(ListNode* head){
    ListNode* pHead = NULL;
    ListNode* t = NULL;
    while(head){
        t = head->next;
        head->next = pHead;
        pHead = head;
        head = t;
    }
    return pHead;
}
```

<h2 id="id3">C++ 容器</h2>

[C++ 中容器总结](http://6924918.blog.51cto.com/6914918/1275726)

C++ 容器包括:**顺序容器**,**关联容器**
**顺序容器:** 将一类元素聚集起来放在容器中,根据位置来存储和访问元素.主要有 vector,list,deque(双端队列).顺序容器适配器:stack,queue和priority_queue

**关联容器:** 通过键来查找读取元素,主要有:pair,set,map,multiset和multimap.


### 顺序容器
**定义**
```
#include <vector>
#include <list>
#include <deque>
vector<int> vi;
list<int> li;
deque<int> di;
```
**初始化**

|  函数模板   | 含义    | 
| :--- | :--- | 
|C c;|创建一个名为c的空容器。C是容器类型名，如vector，T是元素类型，如int或string适用于所有容器。|
|C c(c2);|创建容器c2的副本c；c和c2必须具有相同的容器类型，并存放相同类型的元素。适用于所有容器。|
|C c(b,e);|创建c，其元素是迭代器b和e标示的范围内元素的副本。适用于所有容器。|
|C c(n,t);|用n个值为t的元素创建容器c，其中值t必须是容器类型C的元素类型的值，或者是可转换为该类型的值。只适用于顺序容器|
|C c(n);|创建有 n 个值初始化元素的容器 c。只适用于顺序容器|

**代码实例:**
```
//初始化为一个容器的副本
vector<int> vi;
vector<int> vi2(vi); //利用vi来初始化vi2
//初始化为一段元素的副本
char*words[] = {"stately", "plump", "buck", "mulligan"};
size_twords_size = sizeof(words)/sizeof(char*);
list<string> words2(words, words + words_size);
//分配和初始化指定数目的元素
constlist<int>::size_type list_size = 64;
list<string> slist(list_size, "a"); // 64 strings, each is a
```

**顺序容器操作**
- 插入元素

|函数名|	意义|
| :--- | --- |
|c.push_back(t)|在容器c的尾部添加值为t的元素。返回void 类型|
|c.push_front(t)|在容器c的前端添加值为t的元素。返回void 类型,只适用于list和deque容器类型。|
|c.insert(p,t)|在迭代器p所指向的元素前面插入值为t的新元素。返回指向新添加元素的迭代器。|
|c.insert(p,n,t)|在迭代器p所指向的元素前面插入n个值为t的新元素。返回void 类型|
|c.insert(p,b,e)|在迭代器p所指向的元素前面插入由迭代器b和e标记的范围内的元素。返回 void 类型|

代码实例:
```
//在容器首部或者尾部添加数据
list<int> ilist;
ilist.push_back(ix);//尾部添加
ilist.push_front(ix);//首部添加
//在容器中指定位置添加元素
list<string> lst;
list<string>::iterator iter = lst.begin();
while (cin >> word)
iter = lst.insert(iter, word); // 和push_front意义一样
//插入一段元素
list<string> slist;
string sarray[4] = {"quasi", "simba", "frollo", "scar"};
slist.insert(slist.end(), 10, "A");//尾部前添加十个元素都是A
list<string>::iterator slist_iter = slist.begin();
slist.insert(slist_iter, sarray+2, sarray+4);//指针范围添加
```

- 容器大小

|函数名|意义|
| --- | ---|
|c.size()|返回容器c中元素个数。返回类型为 c::size_type|
|c.max_size()|返回容器c可容纳的最多元素个数，返回类型为c::size_type|
|c.empty()|返回标记容器大小是否为0的布尔值|
|c.resize(n)|调整容器c的长度大小，使其能容纳n个元素，如果n|
|c.resize(n,t)|调整容器c的长度大小，使其能容纳n个元素。所有新添加的元素值都为t|

- 访问元素

|函数名|意义|
| --- | --- |
|c.back()|返回容器 c 的最后一个元素的引用。如果 c 为空，则该操作未定义|
|c.front()|返回容器 c 的第一个元素的引用。如果 c 为空，则该操作未定义|
|c[n]|返回下标为 n 的元素的引用。如果 n <0 或 n >= c.size()，则该操作未定义,只适用于 vector 和 deque 容器|
|c.at(n)|返回下标为 n 的元素的引用。如果下标越界，则该操作未定义,只适用于 vector 和 deque 容器|

- 删除元素

|函数名|意义|
| --- | --- |
|c.erase(p)|删除迭代器p所指向的元素。返回一个迭代器，它指向被删除元素后面的元素。如果p指向容器内的最后一个元素，则返回的迭代器指向容器超出末端的下一位置。如果p本身就是指向超出末端的下一位置的迭代器，则该函数未定义|
|c.erase(b,e)|删除迭代器b和e所标记的范围内所有的元素。返回一个迭代器，它指向被删除元素段后面的元素。如果e本身就是指向超出末端的下一位置的迭代器，则返回的迭代器也指向容器的超出末端的下一位置|
|c.clear()|删除容器c内的所有元素。返回void|
|c.pop_back()|删除容器c的最后一个元素。返回void。如果c为空容器，则该函数未定义|
|c.pop_front()|删除容器c的第一个元素。返回void。如果c为空容器，则该函数未定义,只适用于 list 或 deque 容器|



