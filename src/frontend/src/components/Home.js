import React from "react";

class Home extends React.Component {
    render() {
        const homeStyle = {
            color: "blue",
            margin: 0,
            padding: 0,
            width: '100%',
            display: 'block',
            minHeight: '100%',
            align: 'center'
        };
        return (
            <div style={homeStyle}>
                <h1>We are launching soon</h1>
            </div>
        );
    }
}

export default Home;
