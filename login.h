#ifndef LOGIN_H
#define LOGIN_H

#include <QDialog>
#include <QWebEngineView>
#include <QString>
namespace Ui {
class Login;
}

class Login : public QDialog {
    Q_OBJECT

public:
    explicit Login(QWidget *parent = nullptr);
    ~Login();
    void setSuccess() {
        this->success = true;
    }
    bool getSuccess() {
        return this->success;
    }
private slots:
    void on_pushButton_clicked();
    void cookieAdd(const QNetworkCookie &cookie);

    void on_pushButton_2_clicked();

private:
    Ui::Login *ui;
    bool success = false;
    QWebEngineView *page;
    std::map<QString,QString> cookies;
};

#endif // LOGIN_H
