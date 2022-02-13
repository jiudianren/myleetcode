

/*
 *
 * ����һ������ǰ�������������������������
 *
 *
 *       ����ǰ��������ص�, ֪ǰ������(PreSequence)���׸�Ԫ��(PreSequence[0])Ϊ�������ĸ�(root),
 *        Ȼ������������(InSequence)�в��Ҵ˸�(root),  ������������ص�, ֪�ڲ��ҵ��ĸ�(root) ǰ�ߵ�����Ϊ�����������������������,
 *       ��ߵ�����Ϊ����������������������С� ���������������(InSequence)��ǰ����left��Ԫ��.
 *        ����ǰ������(PreSequence)��, �����Ÿ�(root)��left��Ԫ������(��PreSequence[1...left]) Ϊ������������ǰ���������,
 *        �ں�ߵ�Ϊ������������ǰ���������.������������������ʵ��������������������һ����ֻ�Ǵ�ʱǰ������ΪPreSequence[1...left]),
 *         ��������ΪInSequence[0...left-1], �ֱ�Ϊԭ���е��Ӵ�,
 *        ����������ͬ��, ��Ȼ�����õݹ鷽�������
 * */


/**
 * Definition for a binary tree node.
 */
#include <vector>
using namespace std;
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {

		TreeNode * t = nullptr;

		if( preorder.size()==0)
		{
			return t ;
		}
		auto rootNode= preorder[0];

		auto index =std::find(inorder.begin(), inorder.end(), rootNode);

		vector<int > linorder;
		for( auto  be= inorder.begin(); be != index; be++)
		{
			linorder.push_back( *be);
		}

		vector<int > rinorder;

		for( ; index != inorder.end(); index++)
		{
			rinorder.push_back( *index);
		}


		int llength= linorder.size();
		vector<int> lpreorder;
		for( int i=0 ; i < llength; i++)
		{
			lpreorder.push_back( preorder[i+1]);
		}
		auto rlength =rinorder.size();

		vector<int> rpreorder;
		for( int i=0 ; i < rlength; i++)
		{
			rpreorder.push_back( preorder[ llength+1+i]);
		}

		t=(TreeNode *)malloc(sizeof(TreeNode));
		if(t!= nullptr)
		{
			t->val= rootNode;
			t->left =buildTree(lpreorder,linorder);//�ݹ鴴������
			t->right =buildTree( rpreorder ,rinorder);//�ݹ鴴���Һ���

		}

        return t;
    }

    void pre(TreeNode * t)
    {
    	if( t!= nullptr)
    	{
    		cout<< t->val<<",";
    		pre( t->left);
    		pre( t->right);
    	}

    }
};


int main()
{

	vector<int> pre;
	vector<int > inor;

	pre.push_back(3);
	pre.push_back(9);
	pre.push_back(20);
	pre.push_back(15);
	pre.push_back(7);


	inor.push_back(9);
	inor.push_back(3);
	inor.push_back(15);
	inor.push_back(20);
	inor.push_back(7);

	auto node = Solution().buildTree(pre, inor);
	 Solution().pre(node);



}
