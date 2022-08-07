---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_AYYUBID_DYNASTY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_AYYUBID_DYNASTY
>
> * Class: `PLAYERS`
> * Parameters:
>	* StatementKey `String`

## Samples
```SQL {title="AGENDA_AYYUBID_DYNASTY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_AYYUBID_DYNASTY",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_AYYUBID_DYNASTY",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_10_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_AYYUBID_DYNASTY",
		"StatementKey",
		"AGENDA_AYYUBID_DYNASTY_WARNING"
	);
	
```

