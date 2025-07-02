import click
from rich.console import Console
from rich.syntax import Syntax
from rich.panel import Panel
from rich.table import Table
from pathlib import Path
from typing import Optional
from .generators.iac import IaCGenerator
from .generators.config import ConfigGenerator
from .generators.pipeline import PipelineGenerator
from .generators.utility import UtilityGenerator
from .utils.validators import validate_output

console = Console()

def print_logo():
    """Print AIIAC logo."""
    logo = """
    ╔═══╗╔══╗╔══╗╔═══╗╔═══╗
    ║╔═╗║║╔╗║║╔╗║║╔═╗║║╔═╗║
    ║║─║║║║║║║║║║║║─║║║║─║║
    ║╚═╝║║║║║║║║║║╚═╝║║║─║║
    ║╔═╗║║╚╝║║╚╝║║╔═╗║║╚═╝║
    ╚╝─╚╝╚══╝╚══╝╚╝─╚╝╚═══╝
    AI Infrastructure as Code
    """

@click.group()
@click.version_option(version="0.1.0")
def main():
    """AI Infrastructure as Code Generator"""
    print_logo()

@main.command()
@click.argument('description')
@click.option('--cloud', '-c', default='aws', help='Cloud provider')
@click.option('--type', '-t', default='terraform', help='IaC type')
@click.option('--output', '-o', help='Output directory')
def create(description: str, cloud: str, type: str, output: Optional[str]):
    """Create infrastructure code from description."""
    with console.status("[bold green]Generating infrastructure code..."):
        generator = IaCGenerator()
        result = generator.generate(
            description,
            provider=cloud,
            template_type=type
        )
        
        if result.success:
            _display_and_save_result(result, output)
        else:
            console.print(f"[red]Error:[/] {result.message}")

@main.command()
@click.argument('description')
@click.option('--type', '-t', default='kubernetes', help='Configuration type')
@click.option('--env', '-e', default='dev', help='Environment')
@click.option('--output', '-o', help='Output directory')
def config(description: str, type: str, env: str, output: Optional[str]):
    """Generate configuration files."""
    with console.status("[bold green]Generating configuration..."):
        generator = ConfigGenerator()
        result = generator.generate(
            description,
            config_type=type,
            environment=env
        )
        
        if result.success:
            _display_and_save_result(result, output)
        else:
            console.print(f"[red]Error:[/] {result.message}")

@main.command()
@click.argument('description')
@click.option('--platform', '-p', default='github', help='CI/CD platform')
@click.option('--output', '-o', help='Output directory')
def pipeline(description: str, platform: str, output: Optional[str]):
    """Generate CI/CD pipeline."""
    with console.status("[bold green]Generating pipeline..."):
        generator = PipelineGenerator()
        result = generator.generate(
            description,
            platform=platform
        )
        
        if result.success:
            _display_and_save_result(result, output)
        else:
            console.print(f"[red]Error:[/] {result.message}")

@main.command()
@click.argument('type')
@click.argument('description')
@click.option('--output', '-o', help='Output directory')
def util(type: str, description: str, output: Optional[str]):
    """Generate utility code."""
    with console.status("[bold green]Generating utility..."):
        generator = UtilityGenerator()
        result = generator.generate(
            description,
            utility_type=type
        )
        
        if result.success:
            _display_and_save_result(result, output)
        else:
            console.print(f"[red]Error:[/] {result.message}")

@main.command()
def list():
    """List available generators and templates."""
    table = Table(title="Available Generators")
    
    table.add_column("Type", style="cyan")
    table.add_column("Providers/Platforms", style="green")
    table.add_column("Templates", style="yellow")
    
    # Add rows for each generator type
    table.add_row(
        "Infrastructure",
        "\n".join(["aws", "azure", "gcp"]),
        "\n".join(["terraform", "cloudformation", "bicep"])
    )
    
    table.add_row(
        "Configuration",
        "\n".join(["kubernetes", "docker", "terraform"]),
        "\n".join(["yaml", "compose", "tfvars"])
    )
    
    table.add_row(
        "Pipeline",
        "\n".join(["github", "gitlab", "jenkins"]),
        "\n".join(["workflow", "ci", "jenkinsfile"])
    )
    
    table.add_row(
        "Utility",
        "\n".join(["network", "kubectl", "mongo"]),
        "\n".join(["scanner", "command", "query"])
    )
    
    console.print(table)

def _display_and_save_result(result, output_dir: Optional[str]):
    """Display and optionally save generation result."""
    # Display result
    for template in result.templates:
        syntax = Syntax(
            template.code,
            template.language,
            theme="monokai"
        )
        console.print(Panel(
            syntax,
            title=f"[blue]{template.description}[/]"
        ))
    
    # Save if output directory specified
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        for template in result.templates:
            file_path = output_path / f"{template.type}.{template.language}"
            with open(file_path, 'w') as f:
                f.write(template.code)
            
            console.print(f"[green]✓[/] Saved to: {file_path}")

if __name__ == '__main__':
    main()