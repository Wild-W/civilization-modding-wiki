---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_WITH_SHIELD_OR_ON_IT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_WITH_SHIELD_OR_ON_IT
>
> * Class: `PLAYERS`
> * Arguments:
>	* AgreementValue `Integer`

## Samples

```SQL {title="REQUIRES_PLAYER_WITH_SHIELD_OR_ON_IT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_WITH_SHIELD_OR_ON_IT",
		"REQUIREMENT_PLAYER_WITH_SHIELD_OR_ON_IT"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_WITH_SHIELD_OR_ON_IT",
		"AgreementValue",
		0
	);
	
```
