import "./Footer.css";

function Footer() {

  const openLinkedIn = () => {
    window.open('https://www.linkedin.com/in/luke-connors-981373b1/');
  };

  const openGitHub = () => {
    window.open('https://github.com/LukeConnors');
  };

  return (
    <div className="footer-container">
      <div>
        <a className="footer-logos" href="#" onClick={openLinkedIn}>
          <i id="linkedin" className="fa-brands fa-linkedin-in" style={{ color: "#00d5ae" }}></i>
        </a>

        <a className="footer-logos" href="#" onClick={openGitHub}>
          <i id="github" className="fa-brands fa-github" style={{ color: "#f5bd01" }}></i>
        </a>
      </div>
      <h3 className="footer-name">by: Luke Connors</h3>
    </div>
  );
}

export default Footer;
