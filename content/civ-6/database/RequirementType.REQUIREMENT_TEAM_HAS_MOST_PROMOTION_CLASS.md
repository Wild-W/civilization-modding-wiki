---
tags:
- RequirementType
title: REQUIREMENT_TEAM_HAS_MOST_PROMOTION_CLASS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_TEAM_HAS_MOST_PROMOTION_CLASS
>
> * Class: `TEAMS`
> * Arguments:
>	* PromotionClass `String`
>		* [UnitPromotionClasses.PromotionClassType]

## Samples

```SQL {title="VICTORY_TANKBANKER_REQUIRES_TEAM_HAS_MOST_TANKS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"VICTORY_TANKBANKER_REQUIRES_TEAM_HAS_MOST_TANKS",
		"REQUIREMENT_TEAM_HAS_MOST_PROMOTION_CLASS"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"VICTORY_TANKBANKER_REQUIRES_TEAM_HAS_MOST_TANKS",
		"PromotionClass",
		"PROMOTION_CLASS_HEAVY_CAVALRY"
	);
	
```
