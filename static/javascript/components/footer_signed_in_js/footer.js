class FooterSignedInClass extends HTMLElement {  
  constructor() {
    super();

    // print the variable passed in
    // console.log(this.getAttribute("link_home"));
  }

  connectedCallback() {
    this.innerHTML = `
    <footer class="logged-in-footer-tag">
      <p>Contact: Robert@Triviafy.com | All Rights Reserved. 2021 Triviafy</p>
    </footer>
    `;
  }
}

customElements.define('footer-signed-in-component', FooterSignedInClass);