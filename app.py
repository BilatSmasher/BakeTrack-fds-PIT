
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --brown: #573a2b;
    --brown2: #79543e;
    --cream: #fbf7f0;
    --peach: #f1e4d5;
    --gold: #d6a45f;
    --ink: #33271f;
    --muted: #897b70;
    --line: #eee5dc;
    --white: #fff;
}

 {
    box-sizing: border-box;
}

body {
    display: flex;
    min-height: 100vh;
    margin: 0;
    background: var(--cream);
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}

.sidebar {
    position: fixed;
    inset: 0 auto 0 0;
    display: flex;
    flex-direction: column;
    width: 245px;
    padding: 28px 18px;
    background: #38271f;
    color: var(--white);
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 4px 10px 34px;
}

.brand-mark {
    display: grid;
    place-items: center;
    width: 43px;
    height: 43px;
    border-radius: 14px;
    background: var(--gold);
    color: #38271f;
    font-family: Georgia, serif;
    font-size: 27px;
    font-weight: bold;
}

.brand strong {
    display: block;
    font-size: 19px;
}

.brand small {
    color: #c9b8aa;
    font-size: 11px;
}

.sidebar nav {
    display: grid;
    gap: 7px;
}

.sidebar nav a {
    display: flex;
    align-items: center;
    gap: 13px;
    padding: 13px 14px;
    border-radius: 10px;
    color: #d8c9be;
    font-size: 14px;
    text-decoration: none;
}

.sidebar nav a.active,
.sidebar nav a:hover {
    background: #634633;
    color: var(--white);
}

.sidebar-note {
    margin-top: auto;
    padding: 15px 12px;
    border-top: 1px solid #5c4638;
    color: #bca99b;
    font-family: Georgia, serif;
    font-style: italic;
    line-height: 1.6;
}

.main {
    width: calc(100% - 245px);
    max-width: 1600px;
    margin-left: 245px;
    padding: 30px 38px 20px;
}

.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 25px;
}

.eyebrow {
    color: var(--brown2);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
}

.topbar h1 {
    margin: 5px 0 0;
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 30px;
}

.top-date {
    color: var(--muted);
    font-size: 13px;
}

.hero {
    display: flex;
    min-height: 225px;
    overflow: hidden;
    margin-bottom: 22px;
    border-radius: 18px;
    background: linear-gradient(110deg, #684832, #9a6d4b);
    color: var(--white);
}

.hero-copy {
    flex: 1;
    padding: 27px 32px;
}

.hero h2 {
    margin: 12px 0 8px;
    font: 700 29px 'Playfair Display', Georgia, serif;
}

.hero p {
    max-width: 430px;
    color: #f0e4d8;
    font-size: 13px;
    line-height: 1.6;
}

.hero img {
    width: 34%;
    min-height: 225px;
    object-fit: cover;
    opacity: 0.88;
}

.pill {
    padding: 7px 10px;
    border-radius: 20px;
    background: #ffffff22;
    font-size: 9px;
    letter-spacing: 1.5px;
}

.btn {
    display: inline-block;
    padding: 11px 16px;
    border: 0;
    border-radius: 9px;
    background: var(--brown);
    color: var(--white);
    font: 600 13px 'DM Sans', sans-serif;
    text-decoration: none;
    cursor: pointer;
}

.btn:hover {
    background: #76513b;
}

.btn.light {
    margin-top: 7px;
    background: var(--white);
    color: var(--brown);
}

.btn.secondary {
    margin: 8px 0 12px;
    background: #f1e7dc;
    color: var(--brown);
}

.btn.small {
    padding: 8px 11px;
    font-size: 11px;
}

.stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin-bottom: 22px;
}

.stat,
.panel {
    padding: 19px;
    border: 1px solid var(--line);
    border-radius: 14px;
    background: var(--white);
    box-shadow: 0 4px 15px #55391b08;
}

.stat span {
    display: block;
    color: var(--muted);
    font-size: 12px;
}

.stat strong {
    display: block;
    margin: 8px 0 4px;
    color: var(--brown);
    font-size: 25px;
}

.stat small {
    color: #a3978d;
    font-size: 11px;
}

.two-col {
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    gap: 17px;
    margin-bottom: 18px;
}

.panel {
    margin-bottom: 18px;
}

.panel-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 17px;
}

.panel h3 {
    margin: 0 0 4px;
    font: 700 18px 'Playfair Display', Georgia, serif;
}

.panel-head p {
    margin: 0;
    color: var(--muted);
    font-size: 11px;
}

.panel-head a:not(.btn) {
    color: var(--brown2);
    font-size: 12px;
    text-decoration: none;
}

.photo-panel {
    padding: 0;
    overflow: hidden;
}

.photo-panel img {
    width: 100%;
    height: 145px;
    object-fit: cover;
}

.photo-panel div {
    padding: 15px 18px;
}

.photo-panel p {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.5;
}

.table-wrap {
    overflow-x: auto;
}

table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
    white-space: normal;
}

th {
    padding: 11px 9px;
    border-bottom: 1px solid var(--line);
    color: #9a8b7e;
    font-size: 10px;
    text-align: left;
    text-transform: uppercase;
    letter-spacing: 0.7px;
}

td {
    padding: 13px 9px;
    border-bottom: 1px solid #f3eee8;
    vertical-align: middle;
}

tr:last-child td {
    border-bottom: 0;
}

.stock-low {
    padding: 5px 8px;
    border-radius: 20px;
    background: #fff0eb;
    color: #b44c35;
    font-size: 11px;
}

.stock-good {
    padding: 5px 8px;
    border-radius: 20px;
    background: #edf6ed;
    color: #47754d;
    font-size: 11px;
}

.tag {
    padding: 5px 8px;
    border-radius: 20px;
    background: #f4eee7;
    color: var(--brown2);
    font-size: 10px;
}

.empty {
    padding: 22px;
    color: var(--muted);
    font-size: 12px;
    text-align: center;
}

.alert {
    margin-bottom: 16px;
    padding: 12px 15px;
    border-radius: 9px;
    font-size: 13px;
}

.alert.success {
    background: #edf6ed;
    color: #376b40;
}

.alert.error {
    background: #fff0eb;
    color: #a5412d;
}

.form-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    align-items: end;
    gap: 14px;
}

.form-grid label,
.stack-form label,
.sale-line label {
    display: grid;
    gap: 7px;
    color: #6e5b4c;
    font-size: 11px;
    font-weight: 600;
}

.form-grid input,
.form-grid select,
.stack-form input,
.stack-form select,
.sale-line input,
.sale-line select,
.search input,
.inline-form input {
    width: 100%;
    min-width: 0;
    padding: 10px;
    border: 1px solid #e8ddd2;
    border-radius: 8px;
    background: #fffdfa;
    color: var(--ink);
    font: 13px 'DM Sans', sans-serif;
}

.form-action {
    align-self: end;
}

.search {
    display: flex;
    gap: 7px;
}

.search input {
    width: 170px;
}

.inline-form {
    display: flex;
    min-width: 300px;
    gap: 5px;
}

.inline-form input {
    width: 75px;
    padding: 7px;
}

.hint {
    margin-top: 13px;
    color: var(--muted);
    font-size: 11px;
}

.narrow {
    max-width: 850px;
}

.sale-line {
    display: grid;
    grid-template-columns: 1fr 140px;
    align-items: end;
    gap: 12px;
    margin-bottom: 9px;
    padding: 12px;
    border: 1px solid var(--line);
    border-radius: 10px;
    background: #fcf9f5;
}

.sale-line select,
.sale-line input {
    margin-top: 7px;
}

.remove-line {
    padding: 8px;
    border: 0;
    border-radius: 7px;
    background: #f7e8e3;
    color: #a14b3b;
    cursor: pointer;
}

.spaced {
    margin: 18px 0;
}

.stack-form {
    display: grid;
    gap: 13px;
}

.stack-form .btn {
    justify-self: start;
}

.credit-total {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    margin-bottom: 18px;
    padding: 20px 24px;
    border-radius: 13px;
    background: #684832;
    color: var(--white);
}

.credit-total span {
    font-size: 13px;
}

.credit-total strong {
    font-size: 25px;
}

.user-area {
    display: flex;
    align-items: center;
    gap: 12px;
    color: var(--muted);
    font-size: 12px;
}

.user-area form {
    margin: 0;
}

.login-main {
    width: min(100% - 30px, 900px);
    margin: 0 auto;
    padding-top: 55px;
}

.login-panel {
    max-width: 430px;
    margin: 55px auto;
}

.wide-label {
    display: grid;
    max-width: 280px;
    gap: 7px;
    margin-bottom: 14px;
    color: #6e5b4c;
    font-size: 11px;
    font-weight: 600;
}

.wide-label select {
    padding: 10px;
    border: 1px solid #e8ddd2;
    border-radius: 8px;
    background: #fffdfa;
    font: 13px 'DM Sans', sans-serif;
}


footer {
    padding: 15px 0;
    color: #aa9c90;
    font-size: 10px;
    text-align: center;
}

/* ==============================
   TABLET RESPONSIVENESS
============================== */

@media (max-width: 1000px) {
    .sidebar {
        width: 205px;
    }

    .main {
        width: calc(100% - 205px);
        margin-left: 205px;
        padding: 25px 22px;
    }

    .stats {
        grid-template-columns: repeat(2, 1fr);
    }

    .two-col {
        grid-template-columns: 1fr;
    }

    .form-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* ==============================
   MOBILE RESPONSIVENESS
============================== */

@media (max-width: 650px) {
    body {
        display: block;
    }

    .sidebar {
        position: static;
        width: 100%;
        padding: 12px 14px;
    }

    .brand {
        padding: 3px 4px 12px;
    }

    .sidebar nav {
        display: flex;
        overflow-x: auto;
        gap: 5px;
    }

    .sidebar nav a {
        padding: 9px 11px;
        font-size: 12px;
        white-space: nowrap;
    }

    .sidebar-note {
        display: none;
    }

    .main {
        width: 100%;
        margin: 0;
        padding: 20px 13px;
    }

    .topbar h1 {
        font-size: 25px;
    }

    .top-date {
        font-size: 10px;
    }

    .hero {
        min-height: 190px;
    }

    .hero-copy {
        padding: 20px;
    }

    .hero h2 {
        font-size: 23px;
    }

    .hero img {
        width: 32%;
        min-height: 190px;
    }

    .stats {
        gap: 9px;
    }

    .stat {
        padding: 14px;
    }

    .stat strong {
        font-size: 20px;
    }

    .form-grid {
        grid-template-columns: 1fr;
    }

    .panel {
        padding: 15px;
    }

    .panel-head {
        align-items: flex-start;
        flex-direction: column;
    }

    .search {
        width: 100%;
    }

    .search input {
        flex: 1;
    }

    .sale-line {
        grid-template-columns: 1fr 95px;
    }

    .credit-total strong {
        font-size: 21px;
    }
}
