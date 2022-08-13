---
tags:
- RequirementType
title: REQUIREMENT_ATTACKER_PLOT_IMPROVEMENT_DEFENSE_STRENGTH
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_ATTACKER_PLOT_IMPROVEMENT_DEFENSE_STRENGTH
>
> * Class: `PLOTS`
> * Arguments:
>	* Amount `Integer`

## Samples

```SQL {title="UNIT_IS_OCCUPYING_DEFENSE_IMPROVEMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"UNIT_IS_OCCUPYING_DEFENSE_IMPROVEMENT",
		"REQUIREMENT_ATTACKER_PLOT_IMPROVEMENT_DEFENSE_STRENGTH"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"UNIT_IS_OCCUPYING_DEFENSE_IMPROVEMENT",
		"Amount",
		1
	);
	```
