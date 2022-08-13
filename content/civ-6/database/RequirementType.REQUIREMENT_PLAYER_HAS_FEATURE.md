---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_FEATURE
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_FEATURE
>
> * Class: `PLAYERS`
> * Arguments:
>	* FeatureType `String`
>		* [Features.FeatureType]

## Samples

```SQL {title="PLAYER_HAS_ZHANGYE_DANXIA"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"PLAYER_HAS_ZHANGYE_DANXIA",
		"REQUIREMENT_PLAYER_HAS_FEATURE"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"PLAYER_HAS_ZHANGYE_DANXIA",
		"FeatureType",
		"FEATURE_ZHANGYE_DANXIA"
	);
	
```
