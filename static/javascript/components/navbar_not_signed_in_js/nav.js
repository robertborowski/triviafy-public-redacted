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
          <!-- <li><a href="#">How It Works</a></li> -->
          <li><a href="${this.getAttribute("link_about_js")}">About</a></li>
          <!-- <li><a href="#">Add Triviafy</a></li> -->
          <!-- <li><a href="#"><button class="button-default button-default-color-primary" type="submit" value="submit" onclick="return clickSubmitButtonOnce()">Add Triviafy</button></a></li> -->



          <li><a href="https://slack.com/oauth/v2/authorize?client_id=2010284559270.2041074682000&scope=app_mentions:read,channels:read,chat:write,groups:read,im:read,incoming-webhook,mpim:read,reactions:read,team:read,usergroups:read,users.profile:read,users:read,users:read.email&state=${this.getAttribute("slack_state_uuid_js")}&user_scope="><img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcSet="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" class="slack-image-button-li" /></a></li>





          <!-- <li><a href="https://slack.com/oauth/v2/authorize?client_id=2010284559270.2041074682000&scope=app_mentions:read,channels:history,channels:read,chat:write,groups:read,im:read,incoming-webhook,mpim:read,reactions:read,team:read,usergroups:read,users.profile:read,users:read,users:read.email,chat:write.public&state=${this.getAttribute("slack_state_uuid_js")}&user_scope="><img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcSet="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" class="slack-image-button-li" /></a></li> -->
          
          <!-- <li><div style="text-align:center;"> <a class="typeform-share button" href="https://form.typeform.com/to/NPVjDw88?typeform-medium=embed-snippet" data-mode="popup" style="display:inline-block;text-decoration:none;background-color:#00C096;color:white;cursor:pointer;font-family:Helvetica,Arial,sans-serif;font-size:20px;line-height:50px;text-align:center;margin:0;height:50px;padding:0px 33px;border-radius:12px;max-width:100%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-weight:bold;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;" data-size="100" target="_blank">Add Triviafy </a> </div> <script> (function() { var qs,js,q,s,d=document, gi=d.getElementById, ce=d.createElement, gt=d.getElementsByTagName, id="typef_orm_share", b="https://embed.typeform.com/"; if(!gi.call(d,id)){ js=ce.call(d,"script"); js.id=id; js.src=b+"embed.js"; q=gt.call(d,"script")[0]; q.parentNode.insertBefore(js,q) } })() </script></li> -->

        </ul>
      </div>
    </nav>
    <div class="spacer-navbar-not-signed-in"></div>
    `;
  }
}

customElements.define('nav-not-signed-in-component', NavbarNotSignedInClass);