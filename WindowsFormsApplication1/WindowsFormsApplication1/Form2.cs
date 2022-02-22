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
    public partial class Form2 : Form
    {
        Form1 f1;
        Form3 f3;

        public string text
        {
            get { return textBox2.Text; }
            set { textBox2.Text = value; }
        }

        public Form2(Form1 f1)
        {
            InitializeComponent();
            this.f1 = f1;
        }

        public void Form2_1(Form3 f3)
        {
            this.f3 = f3;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            f1.text += "\r\n" + System.DateTime.Now + " Отправитель " + this.Name + "\r\n" + textBox1.Text;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            f3.text += "\r\n" + System.DateTime.Now + " Отправитель " + this.Name + "\r\n" + textBox1.Text;
        }
    }
}
