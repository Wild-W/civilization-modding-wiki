---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_LEADER_TAG_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_LEADER_TAG_MATCHES
>
> * Class: `PLAYERS`
> * Arguments:
>	* Tag `String`

## Samples

```SQL {title="REQUIREMENT_IS_PIRATE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIREMENT_IS_PIRATE",
		"REQUIREMENT_PLAYER_LEADER_TAG_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIREMENT_IS_PIRATE",
		"Tag",
		"PIRATE_CIVILIZATION"
	);
	
```
