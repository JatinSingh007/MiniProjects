#include<dos.h>
#include<process.h>
#include<fstream.h>
#include<iomanip.h>  
#include<conio.h>
#include<string.h>
#include<stdio.h>
using namespace std;
class emp
{
 char serial[30],contact[12],name[40],designation[40];
 float salary;
 public:
 char* getserial()
 {
  return serial;
 }
 char* getname()
 {
  return name;
 }
 void input();
 void output();
 void edit();
};
//--------------------------
void emp::input()
{
//Used to take Input of employee records 
 cout<<"\n ADD EMPLOYEES DATA ...\n";
 cout<<"\n Employee Code : ";
 gets(serial);
 cout<<" Employee Name : ";
 gets(name);
 cout<<" Employee Job : ";
 gets(designation);
 cout<<" Contact Number : ";
 gets(contact);
 cout<<" Salary :";
 cin>>salary;
}
//--------------------------
void emp::output()
{
  //Used to print employee records 
 cout<<"\n VIEW EMPLOYEE DATA ...\n";
 cout<<"\n Employee Code : ";
 puts(serial);
 cout<<" Employee Name : ";
 puts(name);
 cout<<" Employee Job : ";
 puts(designation);
 cout<<" Contact Number : ";
 puts(contact);
 cout<<" Salary : ";
 cout<<salary;
}
//--------------------------
void emp::edit()
{
  //Used to Update employee records 
 char ch;
 clrscr();
 cout<<"\n MODIFY EMPLOYEE DATA ...\n\n";
 cout<<"\n Employees Current Detail : ";
 cout<<"\n Employee Code : ";
 puts(serial);
 cout<<" Employee Name : ";
 puts(name);
 cout<<" Employee Job : ";
 puts(designation);
 cout<<" Contact Number : ";
 puts(contact);
 cout<<" Salary : ";
 cout<<salary;
 cout<<"\n Do You Wish To Modify This Record(Y/N) : ";
 cin>>ch;
 if (ch=='y'||ch=='Y')
 {
  clrscr();
  cout<<"\n MODIFY EMPLOYEE DATA ...\n\n";
  cout<<"\n ENTER NEW DETAIL OF EMPLOYEE ...\n";
  cout<<"\n Employee Code : ";
  gets(serial);
  cout<<" Employee Name : ";
  gets(name);
  cout<<" Employee Job : ";
  gets(designation);
  cout<<" Contact Number : ";
  gets(contact);
  cout<<" Salary :";
  cin>>salary;
 }
}
//--------------------------
void enter()
{
  //Takes input,then check if already present ,if present then ignore else append
 clrscr();
 int p=0;
 char code[30];
 emp emp1,emp2;
 ofstream fout("EMP.DAT",ios::binary|ios::app);
 emp1.input();
 strcpy(code,emp1.getserial());
 ifstream fin("EMP.DAT",ios::binary);
 fin.read((char*)&emp2,sizeof(emp2));
 while(fin)
 {
  if(strcmp(code,emp2.getserial())==0)
  {
   p=1;
   break;
  }
  fin.read((char*)&emp2,sizeof(emp2));
 }
 if(p==1)
  cout<<"\n This Employee Code Already Exists";
 else
 {
  fout.write((char*)&emp1,sizeof(emp1));
  cout<<"\n New Data Input Successfully!";
 }
 fout.close();
 fin.close();
}
//--------------------------
void display()
{
  //To dispaly the record if present in the file
 clrscr();
 emp emp1;
 char code[30];
 int p=0;
 ifstream fin("EMP.DAT",ios::binary);
 cout<<"\n Enter Employee Code : ";
 gets(code);
 fin.read((char*)&emp1,sizeof(emp1));
 while(fin)
 {
  if(strcmp(code,emp1.getserial())==0)
  {
   emp1.output();
   p=1;
  }
  fin.read((char*)&emp1,sizeof(emp1));
 }
 if(p==0&&strcmp(code,"  ")!=0)
  cout<<"\n NO SUCH EMPLOYEE EXISTS!";
 fin.close();
}
//--------------------------
void mod()
{
  //Used to modify data of emp if present in file
 clrscr();
 char code[30];
 emp emp1;
 long int pos;
 int p=0;
 cout<<"\n Enter Employee Code : ";
 gets(code);
 fstream fil("EMP.DAT",ios::binary|ios::in|ios::out);
 pos=fil.tellg();
 fil.read((char*)&emp1,sizeof(emp1));
 while (fil)
 {
  if (strcmpi(code,emp1.getserial())==0)
   {
    p=1;
    emp1.edit();
    fil.seekp(pos);
    fil.write((char*)&emp1,sizeof(emp1));
   }
  pos=fil.tellg();
  fil.read((char*)&emp1,sizeof(emp1));
 }
 if(p==0&&strcmp(code,"  ")!=0)
  cout<<"\n NO SUCH EMPLOYEE EXISTS!";
 else if(strcmp(code,"  ")!=0)
  cout<<"\n EMPLOYEE DATA EDITED SUCCESSFULLY!";
 fil.close();
}
//--------------------------
void del()
{
 clrscr();
 char ch,code[30];
 emp emp1,emp2;
 int p=0;
 cout<<"\n Enter Employee Code : ";
 gets(code);
 ifstream fin("EMP.DAT",ios::binary);
 fin.read((char*)&emp1,sizeof(emp1));
 while(fin)
 {
  if(strcmp(code,emp1.getserial())==0)
  {
   emp1.output();
   p=1;
  }
  fin.read((char*)&emp1,sizeof(emp1));
 }
 cout<<"\n Do You Wish To Delete This Record(Y/N) : ";
 cin>>ch;
 fin.close();
 if (ch=='y'||ch=='Y')
 {
  ifstream fin("EMP.DAT",ios::binary);
  ofstream fout("EMP_TEMP.DAT",ios::binary);
  fin.read((char*)&emp1,sizeof(emp1));
  while(fin)
  {
   if(!strcmpi(code,emp1.getserial())==0)
    fout.write((char*)&emp1,sizeof(emp1));
   else
    p=1;
   fin.read((char*)&emp1,sizeof(emp1));
  }
  if (p==0&&strcmp(code,"  ")!=0)
   cout<<"\n NO SUCH EMPLOYEE EXISTS! ";
  else if(strcmp(code,"  ")!=0)
   cout<<"\n EMPLOYEE DATA DELETED SUCCESSFULLY!";
  fin.close();
  fout.close();
  remove ("EMP.DAT");
  rename ("EMP_TEMP.DAT","EMP.DAT");
 }
}
//--------------------------
void list()
{
 ifstream fin("EMP.DAT",ios::binary);
 clrscr();
 int i=1;
 emp emp1;
 fin.read((char*)&emp1,sizeof(emp1));
 cout<<"\n    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++";
 cout<<"\n    +"<<setw(30)<<"EMPLOYEE CODE"<<setw(40)<<"EMPLOYEE NAME +";
 while(fin)
 {
  cout<<"\n    +                                                                     +";
  cout<<"\n    +"<<setw(30)<<emp1.getserial()<<setw(39)<<emp1.getname()<<"+";
  fin.read((char*)&emp1,sizeof(emp1));
  if(i%6==0)
  {
   cout<<"\n    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++";
   cout<<"\n\n Press Any Key For Next Page...";
   getch();
   clrscr();
   cout<<"\n    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++";
   cout<<"\n    +"<<setw(30)<<"EMPLOYEE CODE"<<setw(40)<<"EMPLOYEE NAME +";
  }
  if(!fin)
  cout<<"\n    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++";
  ++i;
 }
}
//--------------------------
void main()
{
 emp emp1;
 char ch;
 int n;
 clrscr();
 cout<<"\n +++++++++++++++++++++++++++++++++++++++*++++++++++++++++++++++++++++++++++++++";
 cout<<"\n +             **********************WELCOME**********************            +";
 cout<<"\n +              *************************************************             +";
 cout<<"\n +               ***********************2***********************              +";
 cout<<"\n +                *********************************************               +";
 cout<<"\n +                 *******************OFFICE******************                +";
 cout<<"\n +                   ***************************************                  +";
 cout<<"\n +                    ***************EMPLOYEE**************                   +";
 cout<<"\n +                     ***********************************                    +";
 cout<<"\n +                      *************DATABASE************                     +";
 cout<<"\n +                       *******************************                      +";
 cout<<"\n +                        **********MANAGMENT**********                       +";
 cout<<"\n +                         ***************************                        +";
 cout<<"\n +                          *********PROGRAM*********                         +";
 cout<<"\n +                           ***********************                          +";
 cout<<"\n +                            *********************                           +";
 cout<<"\n +                             *******************                            +";
 cout<<"\n +                              *****************                             +";
 cout<<"\n +                               ***************                              +";
 cout<<"\n +                                *************                               +";
 cout<<"\n +                                 ***********                                +";
 cout<<"\n +                                  *********                                 +";
 cout<<"\n +                                   *******                                  +";
 cout<<"\n +                                    *****                       HELLO USER  +";
 cout<<"\n +++++++++++++++++++++++++++++++++++++++*++++++++++++++++++++++++++++++++++++++";
 getch();
 do
 {
  clrscr();
  cout<<"\n +++++++++++++++++++++++++++++++++++MAIN MENU++++++++++++++++++++++++++++++++++";
  cout<<"\n +                                                                            +";
  cout<<"\n +                               1. Add Record                                +";
  cout<<"\n +                               2. Modify Record                             +";
  cout<<"\n +                               3. Display Specific Record                   +";
  cout<<"\n +                               4. Delete Specific Record                    +";
  cout<<"\n +                               5. List Display                              +";
  cout<<"\n +                               6. Exit...                                   +";
  cout<<"\n +                                                                            +";
  cout<<"\n +++++++++++++++++++++++++++++++++++++++*++++++++++++++++++++++++++++++++++++++";
  cout<<"\n\n Enter Choice(1-5) : ";cin>>n;
  switch(n)
  {
   case 1: enter();
	   break;
   case 2: mod();
	   break;
   case 3: display();
	   break;
   case 4: del();
	   break;
   case 5: list();
	   break;
   case 6: cout<<"\n Saving Changes Please Wait... ";
	   sleep(2);
	   cout<<"\n\n Press Any Key To Exit... ";
	   getch();
	   exit(0);
   default:cout<<"\n Invalid Choice!";
  }
  cout<<"\n\n\n Do You Wish To Go To Main Menu(Y/N) : ";
  cin>>ch;
 }while(ch=='y'||ch=='Y');
 cout<<"\n\n Saving Changes Please Wait... ";
 sleep(2);
 cout<<"\n\n Press Any Key To Exit... ";
 getch();
 exit(0);
}
