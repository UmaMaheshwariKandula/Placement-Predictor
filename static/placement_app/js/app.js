document.addEventListener('DOMContentLoaded', function () {
    const cgpa = document.getElementById('sim-cgpa');
    const coding = document.getElementById('sim-coding');
    const projects = document.getElementById('sim-projects');
    const cgpaValue = document.getElementById('cgpa-value');
    const codingValue = document.getElementById('coding-value');
    const projectsValue = document.getElementById('projects-value');
    const simResult = document.getElementById('sim-result');
    if (cgpa && coding && projects) {
        const update = () => {
            cgpaValue.textContent = cgpa.value;
            codingValue.textContent = coding.value;
            projectsValue.textContent = projects.value;
            const base = 40;
            const total = (parseFloat(cgpa.value) * 7) + (parseInt(coding.value) * 0.3) + (parseInt(projects.value) * 3);
            const percent = Math.min(99, Math.round(base + total / 2));
            simResult.textContent = `Simulated chance ${percent}% based on CGPA, coding and projects.`;
        };
        cgpa.addEventListener('input', update);
        coding.addEventListener('input', update);
        projects.addEventListener('input', update);
        update();
    }
});
