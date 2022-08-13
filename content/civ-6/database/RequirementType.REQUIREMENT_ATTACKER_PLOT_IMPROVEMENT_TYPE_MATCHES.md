---
tags:
- RequirementType
title: REQUIREMENT_ATTACKER_PLOT_IMPROVEMENT_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_ATTACKER_PLOT_IMPROVEMENT_TYPE_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* ImprovementType `String`
>		* [Improvements.ImprovementType]

## Samples

```SQL {title="UNIT_IS_OCCUPYING_FORT_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"UNIT_IS_OCCUPYING_FORT_REQUIREMENT",
		"REQUIREMENT_ATTACKER_PLOT_IMPROVEMENT_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"UNIT_IS_OCCUPYING_FORT_REQUIREMENT",
		"ImprovementType",
		"IMPROVEMENT_FORT"
	);
	```
