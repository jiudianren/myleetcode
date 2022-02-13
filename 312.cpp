

/*
 *
 * ��̬�滮�� Dynamic Programming, DP�������Ż������һ�ֽ��������������״̬�ռ��״̬ת�ơ�
 * ��ν״̬ת����ָÿ���׶ε�����״̬����Ӧ��������Ľ⣩���Դ�֮ǰ��ĳһ���򼸸��׶ε�״̬�еõ���������ʽ��������ӽṹ��
 * ������֮ǰ���״̬����εõ��ģ��ⱻ��֮Ϊ�޺�Ч�ԡ�

DP����������Ī����01��������:

��N����Ʒ��һ������ΪV�ı�������i����Ʒ�ķ�����c[i]����ֵ��w[i]����⽫��Щ��Ʒװ�뱳����ʹ��ֵ�ܺ����

�������ⶨ��״̬����f[i][v]��ʾǰi����Ʒǡ����һ������Ϊv�ı������Ի�õ�����ֵ������״̬ת�Ʒ��̣�

f[i][v]=max{f[i-1][v],f[i-1][v-c[i]]+w[i]}
����ǰi����Ʒ��������Ϊv�ı����С���������⣬��ֻ���ǵ�i����Ʒ�Ĳ��ԣ��Ż򲻷ţ���
��ô�Ϳ���ת��Ϊһ��ֻǣ��ǰi-1����Ʒ�����⡣������ŵ�i����Ʒ����ô�����ת��Ϊ��ǰi-1����Ʒ��������Ϊv�ı����С���
��ֵΪf[i-1][v]������ŵ�i����Ʒ����ô�����ת��Ϊ��ǰi-1����Ʒ����ʣ�µ�����Ϊv-c[i]�ı����С���
��ʱ�ܻ�õ�����ֵ����f[i-1][v-c[i]]�ټ���ͨ�������i����Ʒ��õļ�ֵw[i]��



�� n �����򣬱��Ϊ0 �� n-1��ÿ�������϶�����һ�����֣���Щ���ִ������� nums �С�

����Ҫ����������е�����ÿ�������һ������ i ʱ������Ի�� nums[left] * nums[i] * nums[right] ��Ӳ�ҡ� ����� left �� right ����� i ���ڵ������������š�ע�⵱����������� i ������ left ������ right �ͱ�������ڵ�����

�����ܻ��Ӳ�ҵ����������

˵��:

����Լ��� nums[-1] = nums[n] = 1����ע�����ǲ�����ʵ���ڵ����Բ����ܱ����ơ�
0 �� n �� 500, 0 �� nums[i] �� 100
ʾ��:

����: [3,1,5,8]
���: 167
����: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
 *
 * */

#include <vector>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <string>
#include <memory.h>

using namespace std;

class Solution {
public:
    int maxCoins(vector<int>& nums) {

    		vector<int> newnum;
    		newnum.push_back(1);
    		for(int i =0; i<nums.size(); i++)
    		{
    			newnum.push_back( nums[i] );
    		}
    		newnum.push_back(1);

    		int length= newnum.size();

           int coins[length][length] = {{0}};
           for(int i=0;i <length; i++)
           {
        	   for(int j=0;j <length; j++)
        	   {
        		   coins[i][j] =0;
        	   }
           }

           for(int i=2; i<newnum.size(); i++) {
        	   //���� ÿ�μ���Ŀ�ʼ�ͽ�����Χ�Ĵ�С

        	   //�� i =2;  ��������һ�ֱ���
        	   //�����еľ������Ϊ2����ֵ�����������
        	   //���� val��0-2�� 1-3 2-4,3-5��Щ��˵Ľ�����������֪
        	   //�� i=3 ����� 0-3,1-4,2-5��
        	   //����0-3����ʱ�� val(0-3)= max�� val( 0-2)+ 3�� 0+ val(1-3) ��
               for(int j=0; j+i< newnum.size(); j++) {
                   for(int k=j+1; k<j+i; k++) {

                       coins[j][j+i] =
                    		   std::max(coins[j][j+i], coins[j][k] + coins[k][j+i] +
                    		   newnum[j] * newnum[k] * newnum[j+i]);

                       cout<< i <<","<<k <<","<< j<<","<<j+i<<","<<coins[j][j+i]<<endl;
                   }
               }
           }
           return coins[0][length-1];

    }
};

int main()
{

	vector<int> pre;
	pre.push_back(3);
	pre.push_back(1);
	pre.push_back(5);
	pre.push_back(8);

	cout<<"result"<<Solution().maxCoins(pre);


}
