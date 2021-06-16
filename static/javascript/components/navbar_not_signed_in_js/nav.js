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
          <li><a href="#">About</a></li>
          <!-- <li><a href="#">Add Triviafy</a></li> -->
          <li><a href="#"><button class="button-default button-default-color-primary" type="submit" value="submit" onclick="return clickSubmitButtonOnce()">Add Triviafy</button></a></li>
        </ul>
      </div>
    </nav>
    <div class="spacer-navbar-not-signed-in"></div>
    `;
  }
}

customElements.define('nav-not-signed-in-component', NavbarNotSignedInClass);