

- [链表中倒数第 k 个节点](#a1)

- [反转链表](#a2)



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


<h2 id='a2'>反转链表</h2>


