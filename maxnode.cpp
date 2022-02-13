
/*
 * ���е����ֵ
 *
 *
 *
 *
 *
 * */

struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };



class Solution {
public:

	TreeNode maxNode(TreeNode root) {

        if(root == NULL)//�����ж�root�ڵ��Ƿ�Ϊ�գ��վ�ֱ�ӷ���
            return NULL;

        TreeNode left = root,right = root;//��rootֵ����left��right����Ϊ�����val���Ƚϣ���ֹ����left��right��val�Ƚ�ʱ����null�쳣����������ܾã�
        if(root.left != NULL)
            left = maxNode(root.left);//�ݹ��ȡ���������node
        if(root.right != NULL)
            right = maxNode(root.right);//�ݹ��ȡ���������node
        TreeNode temp = left.val > root.val ? left:root; //�����Ƚ���������rootȡ�����ֵ

        return right.val > temp.val ?right:temp;//�������ֵ���������Ƚ�

    }

};



