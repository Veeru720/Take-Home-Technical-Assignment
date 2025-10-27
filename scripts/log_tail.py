##!/usr/bin/env python3
"""
Log Tail Script for Platform Engineering

Usage:
    python log_tail.py --env dev --app sample-app --follow
    python log_tail.py --env prod --app sample-app --lines 100
"""

import argparse
import subprocess
import sys
from typing import List, Optional

class LogTail:
    def __init__(self, environment: str, app_name: str):
        self.environment = environment
        self.app_name = app_name
        self.namespace = environment
        
    def get_pods(self) -> List[str]:
        """Get list of pods for the application"""
        cmd = [
            "kubectl", "get", "pods",
            "-n", self.namespace,
            "-l", f"app={self.app_name}",
            "-o", "jsonpath={.items[*].metadata.name}"
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            pods = result.stdout.strip().split()
            if not pods:
                print(f"No pods found for app {self.app_name} in {self.environment}")
                sys.exit(1)
            return pods
        except subprocess.CalledProcessError as e:
            print(f"Error getting pods: {e}")
            sys.exit(1)
            
    def tail_logs(self, follow: bool = False, lines: Optional[int] = None):
        """Tail logs from all pods"""
        pods = self.get_pods()
        
        cmd = [
            "kubectl", "logs",
            "-n", self.namespace,
            "-l", f"app={self.app_name}",
            "--prefix=true"
        ]
        
        if lines:
            cmd.extend(["--tail", str(lines)])
        if follow:
            cmd.append("--follow")
            
        try:
            print(f"Tailing logs for {self.app_name} in {self.environment} environment")
            print(f"Pods: {', '.join(pods)}")
            print("-" * 80)
            
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error tailing logs: {e}")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\nLog tailing stopped")

def main():
    parser = argparse.ArgumentParser(description="Tail application logs across environments")
    parser.add_argument("--env", required=True, choices=["dev", "stage", "prod"],
                       help="Environment to tail logs from")
    parser.add_argument("--app", required=True, help="Application name")
    parser.add_argument("--follow", "-f", action="store_true", 
                       help="Follow logs in real-time")
    parser.add_argument("--lines", "-n", type=int, default=50,
                       help="Number of lines to show from the end of logs")
    
    args = parser.parse_args()
    
    # Validate kubectl is available
    try:
        subprocess.run(["kubectl", "version", "--client"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: kubectl is not installed or not in PATH")
        sys.exit(1)
        
    # Validate we can access the cluster
    try:
        subprocess.run(["kubectl", "get", "nodes"], capture_output=True, check=True)
    except subprocess.CalledProcessError:
        print("Error: Cannot connect to Kubernetes cluster. Please check your kubeconfig.")
        sys.exit(1)
    
    tail = LogTail(args.env, args.app)
    tail.tail_logs(follow=args.follow, lines=args.lines)

if __name__ == "__main__":
    main()        

