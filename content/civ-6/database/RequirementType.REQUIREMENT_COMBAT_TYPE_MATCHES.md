---
tags:
- RequirementType
title: REQUIREMENT_COMBAT_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_COMBAT_TYPE_MATCHES
>
> * Class: `COMBATS`
> * Arguments:
>	* CombatType `String`

## Samples

```SQL {title="MELEE_COMBAT_REQUIREMENTS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"MELEE_COMBAT_REQUIREMENTS",
		"REQUIREMENT_COMBAT_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"MELEE_COMBAT_REQUIREMENTS",
		"CombatType",
		"COMBAT_MELEE"
	);
	
```
