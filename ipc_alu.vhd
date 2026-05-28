library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity ipc_alu is
    Port (
        clk         : in  STD_LOGIC;
        rst         : in  STD_LOGIC;
        operand_a   : in  STD_LOGIC_VECTOR(7 downto 0);
        operand_b   : in  STD_LOGIC_VECTOR(7 downto 0);
        opcode      : in  STD_LOGIC_VECTOR(1 downto 0); -- "00"=ADD, "01"=SUB(IPC)
        result      : out STD_LOGIC_VECTOR(7 downto 0);
        vacuum_flag : out STD_LOGIC;                      -- IPC Information Flag
        tier_out    : out STD_LOGIC_VECTOR(7 downto 0)  -- Preserved Context
    );
end ipc_alu;

architecture Behavioral of ipc_alu is
begin
    process(clk, rst)
    begin
        if rst = '1' then
            result      <= (others => '0');
            vacuum_flag <= '0';
            tier_out    <= (others => '0');
        elsif rising_edge(clk) then
            -- Default assignments
            vacuum_flag <= '0';
            tier_out    <= (others => '0');
            
            case opcode is
                when "00" => -- Standard Addition
                    result <= std_logic_vector(unsigned(operand_a) + unsigned(operand_b));
                
                when "01" => -- IPC Reversible Subtraction
                    if operand_a = operand_b then
                        result      <= (others => '0'); -- Numerical value is zero
                        vacuum_flag <= '1';              -- IPC tracking activated
                        tier_out    <= operand_a;        -- Origin context preserved
                    else
                        result      <= std_logic_vector(unsigned(operand_a) - unsigned(operand_b));
                        vacuum_flag <= '0';
                        tier_out    <= (others => '0');
                    end if;
                    
                when others =>
                    result <= (others => '0');
            end case;
        end if;
    end process;
end Behavioral;

