import QtQuick 2.15
import SddmComponents 2.0

Rectangle {
    width: 1920
    height: 1080
    color: "#0b1c2d"

    Image {
        source: "background.png"
        anchors.fill: parent
        fillMode: Image.PreserveAspectCrop
    }

    Column {
        anchors.centerIn: parent
        spacing: 20

        Text {
            text: "P-Linux"
            font.pixelSize: 48
            color: "white"
        }

        TextField {
            id: password
            echoMode: TextInput.Password
            width: 260
        }

        Button {
            text: "Entrar"
            onClicked: sddm.login("pedro", password.text)
        }
    }
}