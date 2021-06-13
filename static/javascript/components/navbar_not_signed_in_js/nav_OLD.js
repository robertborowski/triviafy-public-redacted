class NavbarNotSignedInClass extends HTMLElement {  
  constructor() {
    super();

    // print the variable passed in
    console.log(this.getAttribute("slack_state_uuid_js"));
  }

  connectedCallback() {
    this.innerHTML = `
      <nav class="navbar">
        <div class="name-logo">
          <a href="#"><img src="/static/images/logo/Logo.png" class="triviafy-logo" alt="Triviafy icon"></a>
          <div class="brand-title"><a href="#">Triviafy</a></div>
        </div>
        <a href="#" class="toggle-button">
          <span class="bar top-bar"></span>
          <span class="bar middle-bar"></span>
          <span class="bar bottom-bar"></span>
        </a>
        <div class="navbar-links">
          <ul>
            <li><a href="#">Login</a></li>
            <li><a href="#"><button class="btn btn-create-account">Add Triviafy</button></a></li>
            <a href="https://slack.com/oauth/v2/authorize?scope=incoming-webhook,commands&client_id=2010284559270.2041074682000&state=${this.getAttribute("slack_state_uuid_js")}"><img alt=""Add to Slack"" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" /></a>
          </ul>
        </div>
      </nav>
    `;
  }
}

customElements.define('nav-not-signed-in-component', NavbarNotSignedInClass);