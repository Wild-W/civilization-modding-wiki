---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_PILLAGE_LEAD
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_PILLAGE_LEAD
>
> * Class: `PLAYERS`
> * Arguments:
>	* Ratio `Integer`
>	* MinimumDelta `Integer`

## Samples

```SQL {title="REQUIRES_HAS_HIGH_PILLAGE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_PILLAGE",
		"REQUIREMENT_PLAYER_PILLAGE_LEAD"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_PILLAGE",
		"MinimumDelta",
		5
	),
	(
		"REQUIRES_HAS_HIGH_PILLAGE",
		"Ratio",
		"1.3"
	);
	
```
