class NavbarNotSignedInClass extends HTMLElement {  
  constructor() {
    super();

    // print the variable passed in
    console.log(this.getAttribute("slack_state_uuid_js"));
  }

  connectedCallback() {
    this.innerHTML = `
    <nav class="navbar-not-signed-in box-shadow-sm-grey box-shadow-rounded">
  
      <!-- Logo and Company Name -->
      <div class="company-name-and-logo-navbar-not-signed-in">
        <!-- Logo -->
        <a href="${this.getAttribute("link_home_js")}"><img src="/static/images/logo/Logo.png" class="company-logo-navbar-not-signed-in" alt="Triviafy icon/logo"></a>
        <!-- Company Name -->
        <h1 class="company-name-navbar-not-signed-in"><a href="${this.getAttribute("link_home_js")}">Triviafy</a></h1>
      </div>

      <a href="#" class="toggle-button-not-signed-in">
        <span class="bar top-bar"></span>
        <span class="bar middle-bar"></span>
        <span class="bar bottom-bar"></span>
      </a>

      <!-- Navbar links -->
      <div class="navbar-links-not-signed-in">
        <ul>
          <li class="drill-down"><a href="#">Resources <i class="fas fa-caret-down"></i></a>
            <ul class="box-shadow-reg-primary box-shadow-rounded sub-list-items">
              <li><a href="${this.getAttribute("pdf_example_quiz_js")}">Example Quiz (PDF)</a></li>
              <li><a href="${this.getAttribute("link_faq_js")}">FAQ</a></li>
              <li><a href="${this.getAttribute("link_about_js")}">About</a></li>
              <li><a href="${this.getAttribute("link_privacy_js")}">Privacy</a></li>
            </ul>
          </li>

          <!-- - - - - - - - - - - - - - - - - - - - - - - - - - - Login Modal Start -->
          <!-- <li><a href="#"><p class="modal-login-text" id="login-activate-modal">Login</p></a></li> -->
          <li><a href="#" class="modal-login-text" id="login-activate-modal">Login</a></li>
          <div id="login-details-modal" class="login-modal">
            <div class="login-modal-content box-shadow-reg-black">
              
              <div class="login-modal-header">
                <span class="close-login-modal-x-button">&times;</span>
                <h2>Login</h2>
              </div>
              
              <div class="login-modal-body">
                <ul>
                  <div style="text-align:center;padding:10px 0 0 0"> <a class="typeform-share button" href="https://form.typeform.com/to/NPVjDw88?typeform-medium=embed-snippet" data-mode="popup" style="display:inline-block;text-decoration:none;background-color:white;color:black;border:1px solid rgb(0, 0, 0, 0.20);cursor:pointer;font-family:Helvetica,Arial,sans-serif;font-size:15px;line-height:40px;text-align:center;margin:10px 0 0 0;height:40px;padding:0px 0px;border-radius:5px;width:170px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;" data-size="100" target="_blank">Sign in with <span style="font-weight:bold;">Email</span></a> </div> <script> (function() { var qs,js,q,s,d=document, gi=d.getElementById, ce=d.createElement, gt=d.getElementsByTagName, id="typef_orm_share", b="https://embed.typeform.com/"; if(!gi.call(d,id)){ js=ce.call(d,"script"); js.id=id; js.src=b+"embed.js"; q=gt.call(d,"script")[0]; q.parentNode.insertBefore(js,q) } })() </script>
                  
                  <li><a href="https://slack.com/openid/connect/authorize?response_type=code&scope=openid%20profile%20email&client_id=2010284559270.2041074682000&state=${this.getAttribute("slack_state_uuid_js")}&redirect_uri=https://triviafy.com/slack/oauth_redirect"><img alt="Sign in with Slack" height="40" width="170" src="https://platform.slack-edge.com/img/sign_in_with_slack.png" srcSet="https://platform.slack-edge.com/img/sign_in_with_slack.png 1x, https://platform.slack-edge.com/img/sign_in_with_slack@2x.png 2x" class="slack-image-button-li" /></a></li>
                  
                  <div style="text-align:center;padding:10px 0 10px 0"> <a class="typeform-share button" href="https://form.typeform.com/to/NPVjDw88?typeform-medium=embed-snippet" data-mode="popup" style="text-decoration:none;background-color:white;color:black;cursor:pointer;font-family:Helvetica,Arial,sans-serif;font-size:18px;line-height:40px;text-align:center;margin:10px 0 0 0;height:40px;padding:0px;border-radius:12px;width:170px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-weight:bold;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;" data-size="100" target="_blank"><img height="40" width="170" src="/static/images/microsoft_teams_buttons/sign_in_with_microsoft_teams_170_x_40.png"></a> </div> <script> (function() { var qs,js,q,s,d=document, gi=d.getElementById, ce=d.createElement, gt=d.getElementsByTagName, id="typef_orm_share", b="https://embed.typeform.com/"; if(!gi.call(d,id)){ js=ce.call(d,"script"); js.id=id; js.src=b+"embed.js"; q=gt.call(d,"script")[0]; q.parentNode.insertBefore(js,q) } })() </script>
                </ul>
              </div>
              
              <div class="login-modal-footer">
                <h3>Triviafy</h3>
              </div>
            </div>
          </div>
          <!-- - - - - - - - - - - - - - - - - - - - - - - - - - - Login Modal End -->

          <!-- - - - - - - - - - - - - - - - - - - - - - - - - - - Create Account Modal Start -->
          <!-- <li><a href="#"><p class="modal-create-account-text" id="create-account-activate-modal">Create Account</p></a></li> -->
          <li><a href="#" class="modal-create-account-text" id="create-account-activate-modal">Create Account</p></a></li>
          <div id="create-account-details-modal" class="create-account-modal">
            <div class="create-account-modal-content box-shadow-reg-black">
              
              <div class="create-account-modal-header">
                <span class="close-create-account-modal-x-button">&times;</span>
                <h2>Create Account</h2>
              </div>
              
              <div class="create-account-modal-body">
                <ul>
                  <div style="text-align:center;padding:10px 0 0 0"> <a class="typeform-share button" href="https://form.typeform.com/to/NPVjDw88?typeform-medium=embed-snippet" data-mode="popup" style="display:inline-block;text-decoration:none;background-color:white;color:black;border:1px solid rgb(0, 0, 0, 0.20);cursor:pointer;font-family:Helvetica,Arial,sans-serif;font-size:15px;line-height:40px;text-align:center;margin:10px 0 0 0;height:40px;padding:0px 0px;border-radius:5px;width:139px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;" data-size="100" target="_blank">Add to <span style="font-weight:bold;">Email</span></a> </div> <script> (function() { var qs,js,q,s,d=document, gi=d.getElementById, ce=d.createElement, gt=d.getElementsByTagName, id="typef_orm_share", b="https://embed.typeform.com/"; if(!gi.call(d,id)){ js=ce.call(d,"script"); js.id=id; js.src=b+"embed.js"; q=gt.call(d,"script")[0]; q.parentNode.insertBefore(js,q) } })() </script>
                  
                  <li><a href="https://slack.com/oauth/v2/authorize?client_id=2010284559270.2041074682000&scope=incoming-webhook,team:read,users.profile:read,users:read,users:read.email&state=${this.getAttribute("slack_state_uuid_js")}&user_scope=openid,profile,email"><img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcSet="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" class="slack-image-button-li" /></a></li>
                  
                  <div style="text-align:center;padding:10px 0 10px 0"> <a class="typeform-share button" href="https://form.typeform.com/to/NPVjDw88?typeform-medium=embed-snippet" data-mode="popup" style="text-decoration:none;background-color:white;color:black;cursor:pointer;font-family:Helvetica,Arial,sans-serif;font-size:18px;line-height:40px;text-align:center;margin:10px 0 0 0;height:40px;padding:0px;border-radius:12px;width:139px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-weight:bold;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;" data-size="100" target="_blank"><img height="40" width="139" src="/static/images/microsoft_teams_buttons/add_to_teams_photoshopped.png"></a> </div> <script> (function() { var qs,js,q,s,d=document, gi=d.getElementById, ce=d.createElement, gt=d.getElementsByTagName, id="typef_orm_share", b="https://embed.typeform.com/"; if(!gi.call(d,id)){ js=ce.call(d,"script"); js.id=id; js.src=b+"embed.js"; q=gt.call(d,"script")[0]; q.parentNode.insertBefore(js,q) } })() </script>
                </ul>
              </div>
              
              <div class="create-account-modal-footer">
                <h3>Triviafy</h3>
              </div>
            </div>
          </div>
          <!-- - - - - - - - - - - - - - - - - - - - - - - - - - - Create Account Modal End -->
        </ul>
      </div>
    </nav>
    <div class="spacer-navbar-not-signed-in"></div>
    `;
  }
}

customElements.define('nav-not-signed-in-component', NavbarNotSignedInClass);