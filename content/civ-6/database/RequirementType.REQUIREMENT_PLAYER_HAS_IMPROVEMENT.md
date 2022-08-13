---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_IMPROVEMENT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_IMPROVEMENT
>
> * Class: `Unknown`
> * Arguments:
>	* ImprovementType `Unknown`

## Samples

```SQL {title="REQUIRES_PLAYER_HAS_MAHAVIHARA"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_MAHAVIHARA",
		"REQUIREMENT_PLAYER_HAS_IMPROVEMENT"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_MAHAVIHARA",
		"ImprovementType",
		"IMPROVEMENT_MAHAVIHARA"
	);
	
```
