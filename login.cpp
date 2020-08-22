#include "login.h"
#include "ui_login.h"
#include <QWebEngineView>
#include <QWebEngineProfile>
#include <QMessageBox>
#include <map>
#include <fstream>
#include <QWebEngineCookieStore>
Login::Login(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Login) {
    ui->setupUi(this);
    page = new QWebEngineView(this);
    page->load(QUrl("https://qzone.qq.com/"));
    page->move(ui->label->x(),ui->label->y());
    page->resize(ui->label->geometry().width(),ui->label->geometry().height());
    connect(page->page()->profile()->cookieStore(),&QWebEngineCookieStore::cookieAdded,this,&Login::cookieAdd);
}

Login::~Login() {
    delete ui;
}

void Login::on_pushButton_clicked() {
    using namespace std;
    ofstream out(".\\Python38\\cookie.txt");
    out<<'{'<<endl;
    for(auto &it: cookies) {
        out<<'"'<<it.first.toStdString()<<'"'<<':'<<'"'<<it.second.toStdString()<<'"'<<','<<endl;
    }
    out<<'"'<<"a"<<'"'<<':'<<'"'<<'a'<<'"'<<endl;
    out<<'}'<<endl;
    out.close();
    accept();
}
void Login::cookieAdd(const QNetworkCookie &cookie) {
    cookies[cookie.name()] = cookie.value();
}

void Login::on_pushButton_2_clicked() {
    cookies.clear();
    page->reload();
}
