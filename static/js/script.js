var passwordInput = document.getElementById("password");
var confirmPasswordInput = document.getElementById("confirm_password");
var passwordStrength = document.getElementById("password-strength");
var confirmPasswordError = document.getElementById("confirm_password_error");
var emailInput = document.getElementById('email');

// パスワードの安全性をチェックする関数
function checkPasswordStrength(password) {
    var strength = 0;

    // パスワードの長さチェック
    if (password.length >= 8) {
        strength += 1;
    }
    // 大文字と小文字の使用チェック
    if (/[A-Z]/.test(password) && /[a-z]/.test(password)) {
        strength += 1;
    }
    // 数字の使用チェック
    if (/\d/.test(password)) {
        strength += 1;
    }
    // 特殊文字の使用チェック
    if (/[^A-Za-z0-9]/.test(password)) {
        strength += 1;
    }

    return strength;
}

// パスワードの入力が変更されたときに実行する処理
passwordInput.addEventListener("input", function() {
    var password = passwordInput.value;
    var strength = checkPasswordStrength(password);

    // パスワードの安全性を表示
    if (strength === 0) {
        passwordStrength.innerHTML = "パスワードの安全性：弱";
        passwordStrength.style.color = "red";
    } else if (strength === 1) {
        passwordStrength.innerHTML = "パスワードの安全性：中";
        passwordStrength.style.color = "orange";
    } else if (strength === 2 || strength === 3) {
        passwordStrength.innerHTML = "パスワードの安全性：強";
        passwordStrength.style.color = "green";
    } else if (strength === 4) {
        passwordStrength.innerHTML = "パスワードの安全性：非常に強い";
        passwordStrength.style.color = "darkgreen";
    }
});

// パスワード(確認)の入力が変更されたときに実行する処理
confirmPasswordInput.addEventListener("input", function() {
    var password = passwordInput.value;
    var confirmPassword = confirmPasswordInput.value;

    // パスワードとパスワード(確認)が一致するかどうかをチェック
    if (password === confirmPassword) {
        confirmPasswordError.innerHTML = "";
    } else {
        confirmPasswordError.innerHTML = "パスワードが一致しません";
    }
});



/**
 * フォーカスが外れた場合のイベントハンドラ
 */
emailInput.addEventListener('blur', function(){
  
  // 入力されたメールアドレスを取得してトリムして値を設定し直す
  emailInput.value = emailInput.value.trim();
  
  // 入力チェック
  validate_email();
});

/**
 * メールアドレスの入力チェック
 */
function validate_email() {
  
    var val = emailInput.value;
    
    // 必須チェック
    if (val == "") {
      // エラーメッセージの作成
      var err_msg = document.createElement('p');
      err_msg.textContent = 'メールアドレスは入力必須項目です。';
      
      // エラーメッセージの表示領域
      var err_msg_div = document.getElementById('error-msg-email');
      
      // エラーメッセージの表示領域を表示する
      err_msg_div.style.display = "block";
      
      // エラーメッセージの表示領域にエラーメッセージを追加
      err_msg_div.appendChild(err_msg);
      
      // 入力欄にinput-errorクラスを追加
      emailInput.setAttribute('class', 'input-error');
      
      return;
    }
    // メールアドレス形式チェック
    var regex = new RegExp(/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/);
    if (!regex.test(val)) {
      // エラーメッセージの作成
      var err_msg = document.createElement('p');
      err_msg.textContent = 'メールアドレスを入力してください。';
      
      // エラーメッセージの表示領域
      var err_msg_div = document.getElementById('error-msg-email');
      
      // エラーメッセージの表示領域を表示する
      err_msg_div.style.display = "block";
      
      // エラーメッセージの表示領域にエラーメッセージを追加
      err_msg_div.appendChild(err_msg);
      
      // 入力欄にinput-errorクラスを追加
      emailInput.setAttribute('class', 'input-error');
      
      return;
    }
  }

  /**
 * フォーカスが当たった場合のイベントハンドラ
 */
emailInput.addEventListener('focus', function(){
  
    // input-errorクラスを削除
    emailInput.classList.remove('input-error');
    
    // エラーメッセージの表示領域を非表示にする
    document.getElementById('error-msg-email').style.display = "none";
    
    // エラーメッセージを削除
    document.getElementById('error-msg-email').children[0].remove();
  });


    function sendData() {
        const form = document.getElementById('myForm');
        const formData = new FormData(form);
    
        // FormDataからJSONオブジェクトを作成
        const jsonObject = {};
        formData.forEach((value, key) => {
            jsonObject[key] = value;
        });
        
        console.log("Sending data:", jsonObject);  // デバッグ用

        // fetch('/register', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify(jsonObject)
        // })
        fetch('/register', {
            method: 'POST',
            body: formData  // Content-Type は自動で設定されます
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('登録成功!');
                window.location.href = '/'; // リダイレクト先を設定
            } else {
                alert('エラー: ' + data.message);
            }
        })
        .catch(error => {
            console.error('エラー:', error);
            alert('登録失敗!');
        });
    }