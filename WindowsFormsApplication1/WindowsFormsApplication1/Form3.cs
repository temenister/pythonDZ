using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form3 : Form
    {
        Form1 f1;
        Form2 f2;

        public string text
        {
            get { return textBox2.Text; }
            set { textBox2.Text = value; }
        }

        public Form3(Form1 f1)
        {
            InitializeComponent();
            this.f1 = f1;
        }

        public void Form3_1(Form2 f2)
        {
            this.f2 = f2;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            f1.text += "\r\n" + System.DateTime.Now + " Отправитель " + this.Name + "\r\n" + textBox1.Text;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            f2.text += "\r\n" + System.DateTime.Now + " Отправитель " + this.Name + "\r\n" + textBox1.Text;
        }
    }
}
