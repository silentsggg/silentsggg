# 单链表的结点
class Nodes:
    # 构造方法，初始化结点的value以及指向下一个结点的指针
    def __init__(self, value):
        self.value = value  # self.value中的value为Nodes类的属性，下面的self.next中的next也是
        self.next = None

    # 获取结点值的方法
    def getvalue(self):
        return self.value


# 链表类，指向头结点
class SingleLinkedList:
    # 构造方法，初始化链表指向头结点
    def __init__(self):
        self.headnode = None

    # 获取链表长度
    def getlength(self):
        length = 0
        if self.headnode is None:
            return 0
        node = self.headnode
        while node is not None:
            length += 1
            # 指向下一个结点
            node = node.next
            if node == self.headnode:
                break
        return length

    # 判断链表是否为空
    def isempty(self):
        if self.getlength() == 0:
            return True
        else:
            return False

    # 向链表结尾添加新结点
    def appendnode(self, node: Nodes):
        # 如果是空链表，则将node作为头结点
        if self.isempty():
            self.headnode = node
        else:
            temp = self.headnode
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    # 打印链表
    def prlist(self):
        if self.isempty():
            print('空列表')
        else:
            temp = self.headnode
            while temp is not None:
                print(temp.value)
                temp = temp.next
                if temp == self.headnode:
                    print(temp.value)
                    break

    # 插入结点
    def insertnode(self, node: Nodes, index: int):
        if self.headnode is None:
            print('empty list, please add node into list first')
        else:
            if index == 0:
                # 换头结点
                node.next = self.headnode
                self.headnode = node
            elif 0 < index < self.getlength() - 1:
                # 指向头结点
                nownode = self.headnode
                # 指向index结点
                while index > 1:
                    nownode = nownode.next
                    index -= 1
                # 插入结点
                temp = nownode.next
                nownode.next = node
                node.next = temp
            else:
                print('index error')

    # 输出链表中index位置的结点
    def getnode(self, index: int) -> Nodes:
        if index >= self.getlength():
            print('index out of range')
            return
        # 获取头结点
        elif index == 0:
            node = self.headnode
        else:
            node = self.headnode
            while index > 0:
                node = node.next
                index -= 1
        return node

    # 删除列表中的位于index位置的结点
    def delnode(self, index: int):
        if self.headnode is None:
            print('empty linkedlist,can\'t delete anthing')
        elif index < 0 or index >= self.getlength():
            print('index out of range')
        elif index == 0:
            self.headnode = self.headnode.next
        else:
            # 找到index位置的结点
            node = self.headnode
            '''
            index>0,index-=1, 当index取到0时，node正好位于index结点位置处；
            当index取到1时，node位于index的上一个结点处
            此处使用取到1，因为要知道index结点的上一个节点
            '''
            while index > 1:
                node = node.next  # 这里node取到index位置的上一个结点，即要删除结点的上一个结点
                index -= 1
            # 处理删除
            temp = node.next  # index结点
            node.next = temp.next  # index的上一个结点的next为index的下一个结点
            temp.next = None  # index结点下一个结点为None，剥离


# 实例化链表结点node1-node5
node1 = Nodes(1)
node2 = Nodes(2)
node3 = Nodes(3)
node4 = Nodes(4)
node5 = Nodes(5)

# 实例化单链表list1
list1 = SingleLinkedList()
print(list1.isempty())
list1.prlist()

# 向list1中添加结点
list1.appendnode(node1)
list1.appendnode(node2)
list1.appendnode(node5)
list1.appendnode(node4)

print('----------------添加结点后----------------')
list1.prlist()

print('----------------插入新结点----------------')
node6 = Nodes('hello')
list1.insertnode(node6, 2)
list1.prlist()
print('----------------插入新结点----------------')
list1.insertnode(Nodes('world'), 0)
list1.prlist()

# print('list1_headnode = ', list1.headnode.getvalue())
print('list1链表中索引为3的结点的值为：', list1.getnode(3).getvalue())

print('----------------删除指定index结点----------------')
list1.prlist()
list1.delnode(3)
print('----------------删除后----------------')
list1.prlist()
