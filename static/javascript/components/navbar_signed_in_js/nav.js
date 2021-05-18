class NavbarClass extends HTMLElement {  
  constructor() {
    super();

    // print the variable passed in
    // console.log(this.getAttribute("link_home"));
  }

  connectedCallback() {
    this.innerHTML = `
    <nav class="navbar-signed-in box-shadow-sm-grey box-shadow-rounded">
      <div class="company-name-and-logo">
        <a href="${this.getAttribute("link_home")}"><img src="/static/images/logo/Logo.png" class="company-logo" alt="Triviafy icon/logo"></a>
        <h1 class="company-name"><a href="${this.getAttribute("link_home")}">Triviafy</a></h1>
      </div>
      <a href="#" class="toggle-button">
        <span class="bar top-bar"></span>
        <span class="bar middle-bar"></span>
        <span class="bar bottom-bar"></span>
      </a>
      <div class="navbar-links">
        <ul>
          <li class="drill-down"><a href="#">Score <i class="fas fa-caret-down"></i></a>
            <ul class="box-shadow-reg-primary box-shadow-rounded sub-list-items">
              <li><a href="#">Leaderboard</a></li>
              <li><a href="#">Claim Prize</a></li>
            </ul>
          </li>
          <li class="drill-down"><a href="#">Quiz <i class="fas fa-caret-down"></i></a>
            <ul class="box-shadow-reg-primary box-shadow-rounded sub-list-items">
              <li><a href="#">Feedback</a></li>
              <li><a href="#">Archive</a></li>
              <li><a href="#">Settings</a></li>
            </ul>
          </li>
          <li class="drill-down"><a href="#">Account <i class="fas fa-caret-down"></i></a>
            <ul class="box-shadow-reg-primary box-shadow-rounded sub-list-items">
              <li><a href="#">Subscription</a></li>
              <li><a href="${this.getAttribute("link_account")}">Settings</a></li>
            </ul>
          </li>
        </ul>
      </div>
    </nav>
    `;
  }
}

customElements.define('nav-component', NavbarClass);