class NavbarNotSignedInSlackBetaClass extends HTMLElement {  
  constructor() {
    super();

    // print the variable passed in
    console.log(this.getAttribute("slack_state_uuid_js"));
  }

  connectedCallback() {
    this.innerHTML = `
      <nav class="navbar">
        <ul>
          <a href="https://slack.com/oauth/v2/authorize?scope=incoming-webhook,commands&client_id=2010284559270.2041074682000&state=${this.getAttribute("slack_state_uuid_js")}"><img alt=""Add to Slack"" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" /></a>
        </ul>
      </nav>
    `;
  }
}

customElements.define('nav-not-signed-in-component-slack-beta', NavbarNotSignedInSlackBetaClass);