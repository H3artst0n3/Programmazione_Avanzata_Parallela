#ifndef _NODE_H
#define _NODE_H

struct _tree_node {
  int key;
  void *value;
  struct _tree_node *left;
  struct _tree_node *right;
  struct _tree_node *parent;
};

typedef struct _tree_node *t_node;

t_node make_t_node (void);
void delete_t_node (t_node tmp);
void delete_node_cascade (t_node t);
int node_depth (t_node n);
void s_test (int n);
void r_test (int n);

#endif