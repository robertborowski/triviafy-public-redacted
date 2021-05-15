class NavbarClass extends HTMLElement {  
  constructor() {
    super();

    // print the variable passed in
    // console.log(this.getAttribute("link_home"));
  }

  connectedCallback() {
    this.innerHTML = `
    <nav class="navbar">
      <div class="company-name-and-logo">
        <a href="${this.getAttribute("link_home")}"><img src="/static/images/logo/Logo.png" class="company-logo" alt="Triviafy icon/logo"></a>
        <div class="company-name"><a href="${this.getAttribute("link_home")}">Triviafy</a></div>
      </div>
      <div class="navbar-links">
        <ul>
          <li><a href="#"><i class="fas fa-trophy"></i></a>
            <ul class="trophy-dropdown">
              <li><a href="#">Leaderboard</a></li>
              <li><a href="#">Claim Prize</a></li>
            </ul>
          </li>
          <li><a href="#"><i class="fas fa-edit"></i></a>
            <ul class="quiz-dropdown">
              <li><a href="#">Quiz Feedback</a></li>
              <li><a href="#">Quiz Settings</a></li>
              <li><a href="#">Quiz Archive</a></li>
            </ul>
          </li>
          <li><a href="${this.getAttribute("link_account")}"><i class="fas fa-user-alt"></i></a>
            <ul class="account-dropdown">
              <li><a href="${this.getAttribute("link_account")}">Account</a></li>
              <li><a href="#">Subscription</a></li>
            </ul>
          </li>
        </ul>
      </div>
    </nav>
    `;
  }
}

customElements.define('nav-component', NavbarClass);