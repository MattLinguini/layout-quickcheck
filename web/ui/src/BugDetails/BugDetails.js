import _ from "lodash";
import { FaCheck, FaBug, FaSignInAlt } from "react-icons/fa";
import { useState } from 'react';

import "./BugDetails.css";

export default function BugDetails(props) {

  const [demoVisible, setDemoVisible] = useState(false);

  function toggleDemo() {
    setDemoVisible(!demoVisible);
  }

  let demoSection = <div />;
  if (demoVisible) {
    demoSection = 
      <div className="demo">
        <div className="demo-box">
          <h6>Freshly Reloaded</h6>
          <iframe title="demo_fresh" src={props.data.demo_urls.reloaded}></iframe><br />
          <a target="_blank" href={props.data.demo_urls.reloaded} rel="noreferrer">Open Separately</a>
        </div>
        <div className="demo-box">
          <h6>Dirty Changes</h6>
          <iframe title="demo_changes" src={props.data.demo_urls.dirty}></iframe><br />
          <a target="_blank" href={props.data.demo_urls.dirty} rel="noreferrer">Open Separately</a>
        </div>
      </div>      
  }

  return (
    <div>
      <h4>
        {props.data.bug_type}
        <span className="demo-button" onClick={toggleDemo}>
          <FaSignInAlt />
        </span>
      </h4>

      {demoSection}

      <label>Styles</label> &mdash; <span>{_.join(props.data.styles_used, ', ')}</span>

      <h4>Variants</h4>
      {props.data.variants["Test Variant Details"].map((variant, index) => (
        <div key={index}>
          <span className="variant_status">{(variant.bug_detected && <FaBug className="fail" />) || <FaCheck className="pass" />}</span> <label>{variant.description}</label>
        </div>
      ))}
    </div>
  );
}