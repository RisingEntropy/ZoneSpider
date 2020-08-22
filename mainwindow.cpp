#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "login.h"
#include <QProcess>
#include <QStringList>
#include <string>
#include <QString>
#include <QMessageBox>
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow) {
    ui->setupUi(this);
    ui->num->setValue(10);
}

MainWindow::~MainWindow() {
    delete ui;
}


void MainWindow::on_pushButton_clicked() {
    Login *login = new Login();
    if(login->exec()==QDialog::Accepted) {
        ui->label_2->setText(tr("登陆成功"));
        loged = true;
        ui->pushButton_2->setEnabled(true);
    }
    delete login;
}

void MainWindow::on_pushButton_2_clicked() {
    if(ui->lineEdit_2->text().isEmpty()) {
        QMessageBox::warning(this,tr("错误"),tr("你的QQ不能为空"),QMessageBox::Ok);
    }
    if(ui->lineEdit->text().isEmpty()) {
        QMessageBox::warning(this,tr("错误"),tr("目标QQ不能为空"),QMessageBox::Ok);
    }
    ui->label_2->setText(tr("Working"));
    std::string comm = "Python38\\python.exe Run.py ";
    comm+=ui->lineEdit_2->text().toStdString();
    comm+=' ';
    comm+=ui->lineEdit->text().toStdString()+' '+ QString::number(ui->num->value()).toStdString();
    system(comm.data());
    ui->label_2->setText(tr("开始爬取，注意查看工作目录下的res.xls"));
}
