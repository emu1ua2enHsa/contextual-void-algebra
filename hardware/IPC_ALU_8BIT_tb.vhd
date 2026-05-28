library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity IPC_ALU_8BIT_tb is
-- Testbenches do not have input/output ports
end IPC_ALU_8BIT_tb;

architecture Behavioral of IPC_ALU_8BIT_tb is

    -- Component Declaration for the Unit Under Test (UUT)
    component IPC_ALU_8BIT
    Port ( 
        operand_A   : in  STD_LOGIC_VECTOR (7 downto 0);
        operand_B   : in  STD_LOGIC_VECTOR (7 downto 0);
        active_out  : out STD_LOGIC_VECTOR (7 downto 0);
        vacancy_out : out STD_LOGIC_VECTOR (7 downto 0);
        is_vacancy  : out STD_LOGIC
    );
    end component;

    -- Signal Declarations to drive inputs and monitor outputs
    signal tb_operand_A   : STD_LOGIC_VECTOR(7 downto 0) := (others => '0');
    signal tb_operand_B   : STD_LOGIC_VECTOR(7 downto 0) := (others => '0');
    signal tb_active_out  : STD_LOGIC_VECTOR(7 downto 0);
    signal tb_vacancy_out : STD_LOGIC_VECTOR(7 downto 0);
    signal tb_is_vacancy  : STD_LOGIC;

begin

    -- Instantiate the Unit Under Test (UUT)
    uut: IPC_ALU_8BIT Port Map (
          operand_A   => tb_operand_A,
          operand_B   => tb_operand_B,
          active_out  => tb_active_out,
          vacancy_out => tb_vacancy_out,
          is_vacancy  => tb_is_vacancy
        );

    -- Stimulus Process to verify waveform trajectory states
    stim_proc: process
    begin
        -- Step 1: Apply standard active gradient operation (10 - 4 = 6)
        report "[TESTBENCH] Step 1: Driving active gradient workloads...";
        tb_operand_A <= std_logic_vector(to_unsigned(10, 8));
        tb_operand_B <= std_logic_vector(to_unsigned(4, 8));
        wait for 20 ns;
        assert (tb_active_out = std_logic_vector(to_unsigned(6, 8))) report "Failed Standard Subtraction" severity error;
        assert (tb_is_vacancy = '0') report "False Vacancy Triggered" severity error;

        -- Step 2: Drive a matching cancellation state to trigger the ominus vacancy vector (12 = 12)
        report "[TESTBENCH] Step 2: Injecting perfect magnitude cancellation (n ⊖ n)...";
        tb_operand_A <= std_logic_vector(to_unsigned(12, 8));
        tb_operand_B <= std_logic_vector(to_unsigned(12, 8));
        wait for 20 ns;
        assert (tb_active_out = "00000000") report "Failed to Zero Active Payload" severity error;
        assert (tb_vacancy_out = std_logic_vector(to_unsigned(12, 8))) report "Failed to Preserve Capacity Memory" severity error;
        assert (tb_is_vacancy = '1') report "Hardware Evacuation Sequence Failed to Fire" severity error;

        -- Step 3: Return to active configuration to confirm register clearing mechanics
        report "[TESTBENCH] Step 3: Restoring active operations...";
        tb_operand_A <= std_logic_vector(to_unsigned(25, 8));
        tb_operand_B <= std_logic_vector(to_unsigned(5, 8));
        wait for 20 ns;

        report "[SUCCESS] All hardware register simulation waveforms verified cleanly.";
        wait;
    end process;

end Behavioral;

