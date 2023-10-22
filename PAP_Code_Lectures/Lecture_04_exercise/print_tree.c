#include "print_tree.h"
#include <stdio.h>

void printtree_node(t_node x){
    if (x == NULL){
        printf(".");
        return;
    }
    if (x->right == NULL && x->left == NULL){
        printf("%d", x->key);
        return;
    }
    printf("(%d ", x->key);
    printtree_node(x->left);
    printf(" ");
    printtree_node(x->right);
    printf(")");
}

void print_tree(bst T){
    if (T == NULL){
        return;
    }
    printtree_node(T->root);
    printf("\n");
}